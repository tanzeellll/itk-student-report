from flask import Flask, redirect, url_for, render_template, request, make_response
import pandas as pd
import pdfkit
import json

app = Flask(__name__)

@app.route('/test')
def test():

    # for students who have done exercises up 30%
    # block1 = pd.read_csv('support_files/report_block1.csv')
    # block2 = pd.read_csv('support_files/report_block2.csv')

    # for students who have done exercises down 30%
    # block1 = pd.read_csv('support_files/report_block1_down30.csv')
    # block2 = pd.read_csv('support_files/report_block2_down30.csv')

    # for students who have not done any exercises
    block1 = pd.read_csv('support_files/report_block1_na.csv')
    block2 = pd.read_csv('support_files/report_block2_na.csv')


    with open ('support_files/concepts.json', 'r') as file:
        conceptsJSON = json.load(file)

    ct = conceptsJSON['Computational_Thinking_Concepts']
    pc = conceptsJSON['Programming_Concepts']

    user_id_list = block1['user_id']
    # print(user_id_list)

    for i in user_id_list[0:]:
        result = block1[block1['user_id']==i]
        user_id = result.iloc[0,1]
        name = str(result.iloc[0,2])
        school = str(result.iloc[0,5])
        try:
            grade = int(result.iloc[0,3])
        except ValueError:
            grade = result.iloc[0,3]
        division = result.iloc[0,4]
        

        student_ex = result.iloc[0,6]
        student_lev = result.iloc[0,7]

        school_ex_avg = result.iloc[0,8]
        school_lev_avg = result.iloc[0,9]

    
        filter = block2[block2['user_id']==user_id]
        ex = filter[['exercise_name', 'total_levels', 'levels_done', 'blocks_used', 'description']]
        ex_dict = ex.to_dict(orient='records')

        # filter = block2[block2['user_id']==user_id]
        # concepts = filter[['description']]

        # concepts_list = []

        # for row in concepts['description']:
        #     concepts_list = concepts_list + row.split(',')

        # concepts_list_unique = set(concepts_list)
        # pc = {}
        # ct = {}

        # for c in concepts_list_unique:
        #     print (c)
        #     if c.strip() in conceptsJSON['Programming_Concepts']:
        #         pc[c] = conceptsJSON['Programming_Concepts'][c.strip()]

        #     if c.strip() in conceptsJSON['Computational_Thinking_Concepts']:
        #         ct[c] = conceptsJSON['Computational_Thinking_Concepts'][c.strip()]



        rendered_report = render_template('index.html', name=name, school=school, grade=str(grade), division=division, exAverage=student_ex, levAverage=student_lev, exDict = ex_dict, schoolExAvg=school_ex_avg, schoolLevAvg=school_lev_avg, computationalThinking = ct, programmingConcepts = pc)
        
        # print(rendered_report)
        # with open('renered_op.html', 'w') as f:
            # f.write(rendered_report)
        
        report_name = '_'.join([str(user_id), name.replace(' ', '_').lower(), school.replace(' ', '_').lower()])
        pdfkit.from_string(rendered_report, f'report_na/{report_name}.pdf', options={
            "enable-local-file-access": '', 
            'page-size': 'A4',
            'margin-top': '0',
            'margin-left': '0',
            'margin-right': '0',
            'margin-bottom': '0',
            # 'javascript-delay': '1000',
            # 'print-media-type': '',
            # 'window-status': 'imdone'
            }, css="templates/styles.css")


    # time.sleep(5)
    # response = make_response(pdf_report)
    # response.headers['Content Type'] = 'application/pdf'
    # response.headers['Content-Disposition'] = 'attachment; filename=test.pdf'
    # return response
        
    # return rendered_report
    return "Print Done Successfully!!"


if __name__ == '__main__':
    app.run(debug=True)
