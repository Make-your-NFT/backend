from django.urls import path

from common.views import SignupView, SigninView, UserActivateView, CheckIDView, CheckEmailView

urlpatterns = [
    # ----- Authentication -----
    # 회원가입
    path('signup/', SignupView.as_view()),
    # 로그인
    path('signin/', SigninView.as_view()),
    # 아이디 중복 확인
    path('signup/check/id/', CheckIDView.as_view()),
    # 이메일 인증 링크 전송
    path('signup/check/email/', CheckEmailView.as_view()),
    # 이메일 유효성 검증
    path('activate/<str:uidb64>/<str:token>/', UserActivateView.as_view()),
]
