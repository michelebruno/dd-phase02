import pandas

from utils.change import get_normalized_tags, get_all_petitions, get_petitions_by_tag, get_petitions_by_keyword


def save_target_source(petitions: pandas.DataFrame = get_all_petitions(), filename='target_source.csv'):
    target_source = []

    if not isinstance(petitions, pandas.DataFrame):
        petitions = pandas.DataFrame(petitions)

    for i, p in petitions.iterrows():
        for t in p['tag_names']:
            target_source.append({
                #'source': p['slug'],
                'target': t
            })

    allowed = set([p for i, p in get_normalized_tags().items()])

    target_source = [item for item in target_source if item['target'] in allowed]

    df = pandas.DataFrame(target_source)

    df.to_csv(filename, index=False, encoding='utf-8')


if __name__ == '__main__':
    save_target_source(get_petitions_by_keyword('covid', lang='it-IT')['items'], 'target_source_coronavirus-it-it.csv')
