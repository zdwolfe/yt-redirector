from django.shortcuts import redirect
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return redirect("https://r20---sn-nx57yn7r.googlevideo.com/videoplayback?mt=1448580548&dur=11.052&mv=m&initcwndbps=6302500&ms=au&itag=22&sparams=dur%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cnh%2Cpl%2Cratebypass%2Crequiressl%2Csource%2Cupn%2Cexpire&fexp=9408710%2C9416126%2C9417683%2C9420452%2C9422596%2C9422618%2C9423662&id=o-AFIz_nQrhQTA2_T6e22KZSdwwkpd1h0_i_803O3CucaX&sver=3&ipbits=0&mm=31&ip=23.252.51.116&mn=sn-nx57yn7r&pl=20&ratebypass=yes&lmt=1436154441693027&expire=1448602220&requiressl=yes&mime=video%2Fmp4&source=youtube&upn=ZlhfbrEBvEY&nh=IgpwcjAxLnNlYTAzKgkxMjcuMC4wLjE&signature=C671912781554734F3C50641FA72AF2D67A15520.9C320A77E86B1394BCF004FD4B82B77052B9F4C4&key=yt6")