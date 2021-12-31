import pdfplumber
import re
import mysql.connector

cn = mysql.connector.connect(
    host='localhost', port=3306, db='patent', user='root', password='123456', charset='utf8'
)
cursor = cn.cursor()
DATE = r'\d{4} 年 \d{1,2} 月 \d{1,2} 日'
TEMPLATE = ['一、地理标志产品名称', '二、申请机构', '三、产地范围', '四、质量要求', '五、专用标志使用']


def match(line, rule):
    try:
        return re.search(rule, line).group(0)
    except AttributeError:
        return None


def main(body='', source_from='国家知识产权局'):
    with pdfplumber.open('guo.pdf') as pdf:
        if re.search(DATE, pdf.pages[1].extract_text()) is not None:
            announcement_number = re.search(r'第(...)号', pdf.pages[0].extract_text()).group(0)
            publish_date = re.search(DATE, pdf.pages[1].extract_text()).group(0).replace(' ', '')
            for single_page in pdf.pages[2:]:
                body = body + single_page.extract_text()
        else:
            announcement_number = re.search(r'第(...)号', pdf.pages[0].extract_text()).group(0)
            publish_date = re.search(DATE, pdf.pages[0].extract_text()).group(0).replace(' ', '')
            for single_page in pdf.pages[1:]:
                body = body + single_page.extract_text()
        nodes = body.split('附件')[1:]
        for node in nodes:
            result = []
            row = []
            i = j = 0
            node_rows = node.split('\n')
            while i < len(node_rows) and j < len(TEMPLATE):
                m = match(node_rows[i], TEMPLATE[j])
                if m is not None:
                    result.append(row)
                    row = []
                    j = j + 1
                else:
                    row.append(node_rows[i])
                i = i + 1
            result.append(node_rows[i:])
            product_name = result[1][0].replace('。 ', '')
            applicant = result[2][0].replace('。 ', '')
            production_area = result[3][0].replace('。 ', '')
            qr_str = ''
            for x in result[4]:
                qr_str = qr_str + '\n' + x
            quality_requirements = qr_str
            uodl_str = ''
            for y in result[5]:
                uodl_str = uodl_str + y

            uodl_str = uodl_str.split('。')[0]
            use_of_dedicated_logo = uodl_str
            cursor.execute("INSERT INTO geographical_indication values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                           (0, announcement_number, publish_date, source_from, product_name, applicant, production_area,
                            quality_requirements, use_of_dedicated_logo))
            cn.commit()


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    main()
