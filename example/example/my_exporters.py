from scrapy.exporters import BaseItemExporter
import xlwt

class TxtItemExporter(BaseItemExporter):
    def __init__(self,file,**kwargs):
        self._configure(kwargs)
        self.file=file.name
        type(self.file)
        print(self.file)
        self.wbook=open(self.file,'a',encoding='utf-8')
        # self.wbook=xlwt.Workbook()
        # self.wsheet=self.wbook.add_sheet('scrapy')
        # self.row=0
    def finish_exporting(self):
        self.wbook.close()

    # def start_exporting(self):
        self.wbook=open('spider')
    def export_item(self, item):
        fields=self._get_serialized_fields(item)
        for col,v in enumerate(x for _,x in fields):
            self.wbook.write(v)
        self.wbook.write('\n')
        # self.wbook.write('\n')
        # self.row+=1