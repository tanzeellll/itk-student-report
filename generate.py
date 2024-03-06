from flask import Flask, redirect, url_for, render_template, request, make_response
import pandas as pd
import pdfkit
import time
import os

app = Flask(__name__)

@app.route('/test')
def test():

    block1 = pd.read_csv('final_report_block1.csv')
    block2 = pd.read_csv('report_block2.csv')

    user_id_list = block1['user_id']
    print(user_id_list)

    for i in user_id_list[0:5]:
        result = block1[block1['user_id']==i]
        user_id = result.iloc[0,1]
        name = str(result.iloc[0,2])
        school = result.iloc[0,9]
        grade = int(result.iloc[0,3])
        division = result.iloc[0,4]
        

        student_ex_avg = result.iloc[0,5]
        student_lev_avg = result.iloc[0,6]

        school_ex_avg = result.iloc[0,10]
        school_lev_avg = result.iloc[0,11]

    
        filter = block2[block2['user_id']==user_id]
        ex = filter[["exercise_name", "total_levels", "levels_done", "blocks_used"]]
        ex_dict = ex.to_dict(orient='records')

        # css = ['templates/styles.css']
        rendered_report = render_template('index.html', name=name, school=school, grade=str(grade), division=division, exAverage=student_ex_avg, levAverage=student_lev_avg, exDict = ex_dict, schoolExAvg=school_ex_avg, schoolLevAvg=school_lev_avg)
        # print(rendered_report)

        # with open('renered_op.html', 'w') as f:
            # f.write(rendered_report)
        
        report_name = '_'.join([str(user_id), name.replace(' ', '_').lower()])
        pdfkit.from_string(rendered_report, f'{report_name}.pdf', options={"enable-local-file-access": ''})


    # time.sleep(5)
    # response = make_response(pdf_report)
    # response.headers['Content Type'] = 'application/pdf'
    # response.headers['Content-Disposition'] = 'attachment; filename=test.pdf'
    # return response
        
    return rendered_report
    # return "Print Done Successfully!!"


if __name__ == '__main__':
    app.run(debug=True)
