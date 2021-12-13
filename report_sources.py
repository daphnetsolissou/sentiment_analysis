import json


class SourcesReporter:
    def __init__(self, articles_df):
        self.df = articles_df
        self.report_dict = self.report()

    def report(self):
        unique_sources = self.df['source_name'].unique()
        report_dict = {'totalSources': len(unique_sources),
                       'totalArticles': len(self.df),
                       'sources': self.count_per_sources()
                       }
        return report_dict

    def count_per_sources(self):
        count_sources = self.df['source_name'].value_counts()
        sources_list = []
        for index, value in count_sources.items():
            source_dict = {'name': index,
                           'count': value
                           }
            sources_list.append(source_dict)
        return sources_list

    def get_report_json(self):
        json_object = json.dumps(self.report_dict, indent=2)
        # print(json_object)
        return json_object
