import yaml


def test_data():
    with open(r"C:\Users\Administrator\PycharmProjects\Hogwarts_15demo\testing\cucal.yaml", encoding="utf-8") as f:
        data = yaml.load(f)
        print(data["basedata"]["data1"])
        return data


if __name__ == '__main__':
    test_data()
