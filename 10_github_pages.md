# Github pages란?

Github 레포지토리를 이용해서 손쉽게 웹사이트를 배포할 수 있는 기능이다.

보통 자기소개서나 블로그를 운영할 때 많이 사용한다!

더 자세한 정보는 아래 링크를 참고해주세요.

https://pages.github.com/

# 1. 업로드 하고 싶은 홈페이지 코드를 가져온다.

실제로 코드를 작성해도 좋고,(HTML,CSS,JavaScript 활용) 이미 만들어진 코드를 가져와서 변경해도 좋다.

이번 문서에서는 다운 받아서 활용하도록 하겠다.

https://startbootstrap.com/

### 템플릿 다운 받기

Startbootstap → themes 메뉴 → portfolio-resume 메뉴 - CLARENCE TAYLOR - 다운 받기

![img](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F1af33eb9-307c-4378-be31-26d61a67c941%2FUntitled.png?table=block&id=9a5ad211-182f-4d5d-b21a-8a0134423cb2&spaceId=daa2d103-3ecd-4519-8c30-4f55e74c7ef4&width=2390&userId=01ce277b-2913-450d-ac8a-72ed3070839d&cache=v2)

![img](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fa0cc441f-ee5e-459b-a065-129baed9fbc1%2FUntitled.png?table=block&id=9cd87084-4be5-4e4b-93ea-34b38e539b7a&spaceId=daa2d103-3ecd-4519-8c30-4f55e74c7ef4&width=2390&userId=01ce277b-2913-450d-ac8a-72ed3070839d&cache=v2)

![img](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fea8005a0-00b9-4c63-b74d-6d054905b792%2FUntitled.png?table=block&id=1c27f65d-b2c4-4320-ac2e-cdc4cb559409&spaceId=daa2d103-3ecd-4519-8c30-4f55e74c7ef4&width=2370&userId=01ce277b-2913-450d-ac8a-72ed3070839d&cache=v2)

### 원하는 폴더에 압축을 푼다!

![img](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F5d913f32-6106-4bea-bb0c-a3611b5ede19%2FUntitled.png?table=block&id=f1d8f0e7-fca0-4c27-bf02-19c268427652&spaceId=daa2d103-3ecd-4519-8c30-4f55e74c7ef4&width=1840&userId=01ce277b-2913-450d-ac8a-72ed3070839d&cache=v2)

git bash here 를 이용하거나 macOS의 경우 터미널의 cd 커맨드를 이용해서, 파일이 있는 폴더로 이동한다.

그리고 아래의 명령어를 통해서 commit을 하고 push를 한다.

```jsx
git init
git add .
git commit -m "커밋 메시지"
git remote add origin 레포지토리주소
git push --set-upstream origin master
```

성공했다면 Github 레포지토리에 아래와 같이 출력된다. (파일에 따라 다름)

![img](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fde5b9250-4c65-4450-8558-1b5b0b34b9f3%2FUntitled.png?table=block&id=be8b4ba5-544b-4883-b079-af629992c3c1&spaceId=daa2d103-3ecd-4519-8c30-4f55e74c7ef4&width=2620&userId=01ce277b-2913-450d-ac8a-72ed3070839d&cache=v2)

### Github - Settings - Pages 클릭

![img](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F864d43ef-5b79-4d6a-97de-114e470de241%2FUntitled.png?table=block&id=811d4b74-7c30-4d8b-812b-5d04c7de8a0d&spaceId=daa2d103-3ecd-4519-8c30-4f55e74c7ef4&width=2680&userId=01ce277b-2913-450d-ac8a-72ed3070839d&cache=v2)

### 아래처럼 브랜치 선택 후 Save로 저장

![img](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F2e1950b7-1adf-4c54-877d-393dbdaa6edc%2FUntitled.png?table=block&id=d165b980-b8b8-4def-b192-e734c06a9006&spaceId=daa2d103-3ecd-4519-8c30-4f55e74c7ef4&width=1250&userId=01ce277b-2913-450d-ac8a-72ed3070839d&cache=v2)

### 아래처럼 뜨면 완료

![img](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F80162237-e446-4958-9854-95925eaeed49%2FUntitled.png?table=block&id=307fe2cd-1794-4ac6-8216-fd048b693b75&spaceId=daa2d103-3ecd-4519-8c30-4f55e74c7ef4&width=1370&userId=01ce277b-2913-450d-ac8a-72ed3070839d&cache=v2)

![img](https://www.notion.so/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fc8742da0-b934-492a-b542-27f00288a169%2FUntitled.png?table=block&id=030f66e7-e958-47b4-9fba-9627aba1dc2b&spaceId=daa2d103-3ecd-4519-8c30-4f55e74c7ef4&width=3190&userId=01ce277b-2913-450d-ac8a-72ed3070839d&cache=v2)

