from django.http import JsonResponse
from datetime import datetime,timezone

def index(request)->JsonResponse:
    slack_name = request.GET.get('slack_name','InvestorTim')
    track = request.GET.get('track','backend')
    utc_time = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    current_day = datetime.now().strftime('%A')
    github_file_url= ''
    github_repo_url = ''

    response = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': utc_time,
        'track': track,
        'github_file_url': github_file_url,
        'github_repo_url': github_repo_url,
        'status_code': 200,
    }
    return JsonResponse(response)
