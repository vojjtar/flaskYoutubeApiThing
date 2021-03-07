from flask import Flask, render_template, send_file, request, redirect, url_for, jsonify

import multiprocessing, time, os, glob

from waitress import serve

app = Flask(__name__, template_folder='frontEnd/templates', static_folder='frontEnd/static')

from download.downloadAudio import audio, video, getInfo, deletIllegalSymbols



def cleanDownloadFolder():
    time.sleep(2000)
    dwnDir = glob.glob('download/dwn/*')
    for file in dwnDir:
        os.remove(file)
    print('i cleaned the download directory.')




@app.route('/', methods=['POST', 'GET'])
def mainPage():
    if request.method == 'POST':
        url = request.form['urlInp']

        if request.form['downBut'] == 'downloadAudio':
            return downloadMedia(url, 'audio')
        elif request.form['downBut'] == 'downloadVideo':
            return downloadMedia(url, 'video')

    else:
        return render_template('index.html')


@app.route('/download')
def downloadMedia(urlLink, type):
    if (type == 'video'):
        extension = 'mp4'
        fileName = video(urlLink)
    elif (type == 'audio'):
        extension = 'mp3'
        fileName = audio(urlLink)
    
    return send_file(filename_or_fp=f"download/dwn/{fileName}.{extension}", as_attachment=True)



@app.route('/apiRequestDownload', methods=['POST', 'GET'])
def downloadApi():
    url = request.args.get('url')
    type = request.args.get('type')

    if (type == 'audio'):
        return downloadMedia(url, 'audio')
    elif (type == 'video'):
        return downloadMedia(url, 'video')

@app.route('/apiRequestInfo', methods=['POST', 'GET'])
def sendInfo():
    url = request.args.get('url')
    dataJson = getInfo(url)

    return jsonify(dataJson)




def flaskRun():
    app.run(debug=True)
    #serve(app, host=yourip, port = yourport)


if __name__ == '__main__':
    #cleanDownloadFolder()
    flaskProcess = multiprocessing.Process(name='p1', target=flaskRun)
    deleFilesProcess = multiprocessing.Process(name='p', target=cleanDownloadFolder)
    flaskProcess.start()
    deleFilesProcess.start()
    

