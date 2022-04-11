import pandas as pd


def get_data_frame():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    data_frame = pd.read_csv('./df_male_trimmed.csv')
    return data_frame


def get_height_sizes(data_frame):
    height_size = []
    for total_height in data_frame['height_cm']:
        if 170 <= total_height < 178:
            height_size.append('small')
        elif 174 >= total_height < 182:
            height_size.append('medium')
        elif 1076 >= total_height < 186:
            height_size.append('large')
        elif 178 <= total_height < 190:
            height_size.append('x-large')
        elif 180 <= total_height < 194:
            height_size.append('xx-large')
        elif total_height > 196:
            height_size.append('xxx-large')
        elif total_height < 169:
            height_size.apped('x-small')
    return height_size


def get_weight_sizes(data_frame):
    weight_size = []
    for total_weight in data_frame['weight_hg']:
        if 550 >= total_weight < 650:
            weight_size.append('small')
        elif 650 >= total_weight < 750:
            weight_size.append('medium')
        elif 750 >= total_weight < 850:
            weight_size.append('large')
        elif 850 >= total_weight < 900:
            weight_size.append('x-large')
        elif 900 >= total_weight < 950:
            weight_size.append('xx-large')
        elif total_weight > 1000:
            weight_size.append('xxx-large')
        elif total_weight < 550:
            weight_size.append('x-small')
    return weight_size


def get_waist_sizes(data_frame):
    waist_size = []
    for waist in data_frame['waist_circumference']:
        if 790 >= waist < 840:
            waist_size.append('small')
        elif 840 >= waist < 890:
            waist_size.append('medium')
        elif 890 <= waist < 940:
            waist_size.append('large')
        elif 940 <= waist < 990:
            waist_size.append('x-large')
        elif 990 <= waist < 1040:
            waist_size.append('xx-large')
        elif waist > 1050:
            waist_size.append('xxx-large')
        elif waist < 780:
            waist_size.append('x-small')
    return waist_size


def get_chest_sizes(data_frame):
    chest_size = []
    for chest in data_frame['chest_circumference']:
        if 910 >= chest < 960:
            chest_size.append('small')
        elif 960 >= chest < 1010:
            chest_size.append('medium')
        elif 1010 >= chest < 1060:
            chest_size.append('large')
        elif 1060 >= chest < 1110:
            chest_size.append('x-large')
        elif 1110 >= chest < 1170:
            chest_size.append('xx-large')
        elif chest > 1180:
            chest_size.append('xxx-large')
        elif chest < 900:
            chest_size.append('x-small')
    return chest_size

def main():
    # fething the dataframe
    python_data_frame = get_data_frame()

    height_sizes = get_height_sizes(python_data_frame)
    weight_sizes = get_weight_sizes(python_data_frame)
    waist_sizes = get_waist_sizes(python_data_frame)
    chest_sizes = get_chest_sizes(python_data_frame)

    print(height_sizes)
    print(weight_sizes)
    print(waist_sizes)
    print(chest_sizes)




if __name__ == "__main__":
    main()
