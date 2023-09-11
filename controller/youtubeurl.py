from flask import Blueprint, jsonify, request
from pytube import YouTube

app_flask_yt = Blueprint('app_flask_yt', __name__)

from middleware.auth import check_access

@app_flask_yt.route('/youtube', methods=['GET'])
@check_access
def get_video_youtube():
    try: 
        videoUrl = request.args.get('url')
        videoRes = request.args.get('res')

        if(videoUrl == None):
            return jsonify({'message': 'Url Tidak Boleh Bernilai Null !'})

        if(videoRes == None):
            return jsonify({'message': 'Argumen ?res= Tidak Boleh Kosong !'})

        videoResValidate = None

        if videoRes == '360p':
            videoResValidate = '18'
        elif videoRes == '720p':
            videoResValidate = '22'
        elif videoRes == '1080p':
            videoResValidate = '137'
        else:
            return jsonify({'message': 'Invalid Video Resolution'})

        yt = YouTube(videoUrl)
        get_urlLinks = yt.streams.get_by_itag(videoResValidate).url

        channelVideo = yt.channel_url
        channelVideoId = yt.channel_id
        videoTitle = yt.title
        videoDesc = yt.captions.get_by_language_code('en')

        response = { 
            'dataDetail': [
                {
                'urlLinks': get_urlLinks,
                'videoRes': videoRes,
                'videoResId': videoResValidate
                },
                {
                'videoChannel': channelVideo,
                'videoChannelId': channelVideoId,
                'videoTitle': videoTitle,
                'videoDesc': videoDesc
                }
            ]
        }

        if get_urlLinks == None:
            return jsonify({'message': 'Terjadi Kesalahan Saat Mengurai Data !'})
        else:
            return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)})

