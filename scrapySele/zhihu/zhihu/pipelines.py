import xlwt


class ZhihuPipeline:
    def __init__(self):
        self.row = 1
        # 1.创建workbook对象
        self.book = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.book.add_sheet('CVE', cell_overwrite_ok=True)
        self.sheet.write(0, 0, 'title')

    def process_item(self, item, spider):
        self.sheet.write(self.row, 0, item['title'])
        self.row += 1
        self.book.save('output.xls')
        return item
