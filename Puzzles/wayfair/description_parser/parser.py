import pandas as pd

# def parse_map_type(map_type):


def parse_ca(value):
    value = value.strip()
    if value == 'Not Applied to options NOR Tied to option category':
        return 0, 0
    elif value == 'Applied to options AND Tied to option category':
        return 1, 1
    elif value == 'Applied to options':
        return 1, 0
    elif value == 'Tied to option category':
        return 0, 1
    elif value == 'NULL':
        return 'N', 'N'


def generate_hash(t):
    return '-'.join(map(str, t))


def parse_type(value, t, rule_no):
    value = value.strip()
    if value == 'Non-generic':
        t0 = (0,) + t[:4]
        return [(rule_no,) + t0 + (generate_hash(t0),) + t[4:]]
    elif value == 'Generic':
        t1 = (1,) + t[:4]
        return [(rule_no,) + t1 + (generate_hash(t1),) + t[4:]]
    elif value == 'All':
        t0 = (0,) + t[:4]
        t1 = (1,) + t[:4]
        return [(rule_no,) + t1 + (generate_hash(t1),) + t[4:],
                (rule_no,) + t0 + (generate_hash(t0),) + t[4:]]


def parse_flag(value):
    value = value.strip()
    return 0 if value == 'No' else 1


def parse_rule(value):
    one = 'Copy_Variation_Class_Answer_Rule_Processor'
    two = 'Associate_Principal_Options_Rule_Processor'
    three = 'Blank_Class_Answer_Rule_Processor'

    c_args_oc = 'optionCategoryID'
    c_args_unapplied = 'unapplied optionIDs'
    p, a = -1, ''
    if one in value and two in value:
        p = 5
    elif one in value and three in value:
        p = 6
    elif two in value and three in value:
        p = 7
    elif one in value:
        p = 1
    elif two in value:
        p = 2
    elif three in value:
        p = 3

    if p in [1, 5, 6]:
        if c_args_oc in value and c_args_unapplied in value:
            a = 3
        elif c_args_oc in value:
            a = 1
        elif c_args_unapplied in value:
            a = 2
    return p, a


def main():
    df = pd.read_csv('source_data.csv', na_filter=False)
    r = []

    for index, row in df.iterrows():
        rule_no = row['Rule #']
        if rule_no == 8:
            continue
        source1, source2 = parse_ca(row['Source Class Answer'])
        # target1 = row['Target Class Answer']
        target1, target2 = parse_ca(row['Target Class Answer'])
        rule, arguments = parse_rule(row['Name rule'])
        flagged = parse_flag(row['Flagged?'])

        existing = (source1, source2, target1, target2, rule, arguments, flagged)
        li = parse_type(row['Class Question Map Type'], existing, rule_no)

        r.extend(li)

    output_cols = ['Rule #', 'Generic', 'Applied to Options', 'Applied To Categories', 'Applied to Options',
                   'Applied to Categories',	'HASH',	'Processors', 'Arguments', 'Needs Review']

    output = pd.DataFrame(r, columns=output_cols)

    output.to_csv('output.csv')


main()
