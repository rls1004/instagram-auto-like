# instagram-auto-like
instargram auto like bot.  
youtube => https://youtu.be/JIrvDkwf3C0  
  
If you use it a lot, your activity may be restricted for a certain period of time or your account may be blocked by Instagram, so please be careful.  
  
Just Fun. Don't take it seriously.  
  
오래 돌리거나 많이 사용하면 활동이 제한되거나 계정이 차단 될 수 있으니 그냥 재미로만 보세요 😀 

## What is Instagram?
인스타그램은 언제든지 휴대 전화를 열어서 광고를 볼 수 있는 어플리케이션 입니다. 사진을 게시할 수 있는 기능도 들어있습니다.  

## 코드 설명
### auto-like&#46;py
Automatically clicks the Like button using the `desktop chrome browser` and `selenium`.  

*Problem* : If too many requests are sent, error 429 occurs. then you will no longer be able to send requests for about a day. I don't know the exact limit of 'too many requests'.
  
### auto-like-multiple-tags&#46;py
Selectively click the Like button by browsing two or more tag combinations.  

*Problem* : Same with auto-like&#46;py

### auto-like-mobile-v1&#46;py
Automatically click the Like button through `Instagram application` using `Android emulator`.  
Selenium is not required.  

*Problem* : Not fun, Not cool, Not sexy

### auto-like-mobile-v2&#46;py
Using the `desktop chrome browser` and `selenium`, get the url of the post to click the like button.
Open the obtained url with the `Instagram app` of the `Android emulator` and click the Like button.  

*Problem* : If you send too many requests, your mobile will no longer be able to open the post's url for a while. (I do not know the exact period)
