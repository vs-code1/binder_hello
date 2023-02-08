import xml.etree.ElementTree as ET

# This is the parent (root) tag
# onto which other tags would be
# created
def write_xml(url, bread, que, que_d, opt, ans, exp):
    data = ET.Element('data')


    # subtag
    post_url = ET.SubElement(data, 'postUrl')
    post_url.text = url

    if ' ' in bread:
        x = 1
        new_bread = bread.split(',')
        for item in new_bread:
            crum_bread = ET.SubElement(data, f'crumbread{x}')
            crum_bread.text = item
            x += 1
    else:
        crum_bread = ET.SubElement(data, f'crumbread')
        crum_bread.text = bread

    

    question = ET.SubElement(data, 'question')
    question.text = str(que)

    question_detail = ET.SubElement(data, 'questionDetail')
    question_detail.text = str(que_d)

    options = ET.SubElement(data, 'options')
    options.text = str(opt)

    answer = ET.SubElement(data, 'answer')
    answer.text = str(ans)

    explain = ET.SubElement(data, 'explain')
    explain.text = str(exp)

    b_xml = ET.tostring(data)

    # Opening a file under the name `items2.xml`,
    # with operation mode `wb` (write + binary)
    with open("data.xml", "ab") as f:
        f.write(b_xml)