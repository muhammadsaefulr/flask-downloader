from flask import Blueprint, jsonify, request
import instaloader

app_flask_insta = Blueprint('app_flask_insta', __name__)

from middleware.auth import check_access

@app_flask_insta.route('/instagram', methods=['GET'])
@check_access
def get_post_instagram():
    try:
        postUrl = request.args.get('url')
        loader = instaloader.Instaloader()
        url = postUrl

        shortcode = url.split('/')[4].split('?')[0]
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        
        username_url = post.owner_username
        post_url = post.video_url
        desc_url = post.caption
        thumbnail_url = post.url

        response = {
            'dataDetail': [
                {
                'username': username_url,
                'postUrl': post_url,
                'thumbnailUrl': thumbnail_url,
                'postDesc': desc_url
                }

            ]
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 501
