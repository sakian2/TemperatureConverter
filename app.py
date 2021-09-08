from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/')
def main():
    return render_template('app.html')

@app.route('/send', methods=['POST'])


def send(sum=sum):
   
   #All Functions Here
    def toFahrenheit():
        if (input_temp_unit=="Celsius"):
            answer = ((input_temp * 9/5) + 32)
            if (answer==student_response):
                result = "correct"
            else:
                result = "incorrect"
        if (input_temp_unit=="Rankine"):
            answer = (input_temp - 459.67)
            if (answer==student_response):
                result = "correct"
            else:
                result = "incorrect"
        if (input_temp_unit=="Kelvin"):
            answer = ((input_temp * 9/5) - 459.67)
            if (answer==student_response):
                result = "correct"
            else:
                result = "incorrect"
        return result

    def toKelvin():
        if (input_temp_unit=="Celsius"):
            answer = (input_temp + 273.15)
            if (answer==student_response):
                result = "correct"
            else:
                result = "incorrect"
        elif (input_temp_unit=="Fahrenheit"):
            answer = ((input_temp * 9/5) - 459.67)
            if (answer==student_response):
                result = "correct"
            else:
                result = "incorrect"
        elif (input_temp_unit=="Rankine"):
            answer = (input_temp * 5/9)
            if (answer==student_response):
                result = "correct"
            else:
                result = "incorrect"
        return result

    def toRankine():
        if (input_temp_unit=="Celsius"):
            answer = ((input_temp + 273.15) * 9/5)
            if (answer==student_response):
                result = "correct"
            else:
                result = "incorrect"
        elif (input_temp_unit=="Fahrenheit"):
            answer = input_temp + 459.67
            a = ("%.2f" % answer)
            print (a)
            if (a==student_response):
                result = "correct"
            else:
                result = "incorrect"
        elif (input_temp_unit=="Kelvin"):
            answer = input_temp * 9/5
            if (answer==student_response):
                result = "correct"
            else:
                result = "incorrect"
        return result

    def toCelsius():
        if (input_temp_unit=="Kelvin"):
            answer = (input_temp - 273.15)
            if (answer==student_response):
                result = "correct"
            else:
                result = "incorrect"
        elif (input_temp_unit=="Fahrenheit"):
            answer = ((input_temp - 32) * 5/9)
            if (answer==student_response):
                result = "correct"
            else:
                result = "incorrect"
        elif (input_temp_unit=="Rankine"):
            answer = ((input_temp - 491.67) * 5/9)
            if (answer==student_response):
                result = "correct"
            else:
                result = "incorrect"
        return result
    
  
    if request.method == 'POST':
        input_temp = float(request.form['input_temp'])
        input_temp_unit = request.form['input_temp_unit']
        output_temp_unit = request.form['output_temp_unit']
        student_response = float(request.form['student_response'])

        if (output_temp_unit=='Fahrenheit'):
            sum =  toFahrenheit()
            return render_template('app.html', sum=sum)

        elif (output_temp_unit=='Celsius'):
            sum =  toCelsius()
            return render_template('app.html', sum=sum)

        elif (output_temp_unit=='Kelvin'):
            sum =  toKelvin()
            return render_template('app.html', sum=sum)

        elif (output_temp_unit=='Rankine'):
            sum =  toRankine()
            return render_template('app.html', sum=sum)

        else:
            sum = 'Invalid'
            return render_template('app.html', sum=sum)


if __name__ == ' __main__':
    app.debug = True
    app.run()