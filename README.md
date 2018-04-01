# newbie
# git을 시작하는 방법
1. git을 설치한다.
http://msysgit.github.com/

2. cmd(terminal)창에서 이름, 메일주소 설정하고 확인
git config --global user.name "이름"
git config --global user.email "깃허브 메일주소" 
git config --list

3. git 폴더를 만들 상위폴더로 가서 git폴더를 만듬
cd C:\
mkdir git

4. git 폴더로 이동해서 git 을 이용할 디렉토리로 지정
cd git
git init 

5. github 에 생성한 저장소들 내려받기, 해당 폴더로 이동
git clone git://github.com/smallerhand/python1.git
cd python1

6. 내가 만든 파이썬 파일들 해당 폴더로 옮긴 다음에 add, commit, push
git add *.py
git commit -m all
git push https://github.com/smallerhand/python1.git

#이상 git의 제일 basic한 사용법이었습니다.
#참고
https://nolboo.kim/blog/2013/10/06/github-for-beginner/
https://git-scm.com/book/ko/v1/Git%EC%9D%98-%EA%B8%B0%EC%B4%88