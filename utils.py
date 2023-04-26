def nice_table(dict, title=''):
    '''
    Given a dictionary, it returns an HTML tables with the key-value pairs arranged in rows or columns.
    '''
    
    html = f'<h2 style="text-align:left;">{title}</h2>'
    html += '<table style="width:50%; border-collapse: collapse; font-size: 16px; text-align:center; padding: 10px; border: 1px solid #fff;">'
    html += '<tr>'
    for key, value in dict.items():
        html += f'<td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; border-right: 1px solid #fff;">{key}</td>'
    html += '</tr>'
    
    
    for i in range(max([len(value) for value in dict.values()])):
        html += '<tr>'
        for key, value in dict.items():
            html += f'<td style="border: 1px solid #fff; text-align:center; padding: 10px; color: white; opacity: 0.8; border-left: 1px solid #fff;">{value[i]}</td>'
        html += '</tr>'
            
    return html

