# GIT 시작하기 
### git을 시작하는 가장 쉬운 방법
##### (진짜 시작만 하는 거예요 ^^;;)

### 1. git을 설치한다. <br/>
> http://msysgit.github.com/ <br/>
> 여기서 다운받으세요 :) <br/>

### 2. cmd(terminal)창에서 이름, 메일주소 설정하고 확인 <br/>
> git config --global user.name "이름" <br/> 
> git config --global user.email 깃허브 메일주소 <br/> 
> git config --list <br/>

### 3. git 폴더를 만들 상위폴더로 가서 git폴더를 만듬 <br/>
> cd C:\ <br/>
> mkdir git <br/>
> (git에 연동시킬 폴더를 만들어주세요) <br/>

### 4. git 폴더로 이동해서 git 을 이용할 디렉토리로 지정 <br/>
> cd git <br/>
> (git에 연동시킬 폴더(위에서 만든)로 들어가주세요)<br/>
> git init <br/>

### 5. github 에 생성한 저장소들 내려받기, 해당 폴더로 이동 <br/>
> git clone git://github.com/smallerhand/python1.git <br/>
> cd python1 <br/>

### 6. 내가 만든 파이썬 파일들 해당 폴더로 옮긴 다음에 add, commit, push <br/>
> git add *.py <br/>
> (만약 모든 형식의 파일을 올리고 싶다면, *.py 대신 -A 또는 --all을 씁니다. git add -A 이렇게.) <br/>
> git commit -m all <br/>
> git push https://github.com/smallerhand/python1.git <br/>

### 7. github 상에서 python1 repository안에 있는 파일을 수정했을 때. <br/>
> cd python1 <br/>
> git pull https://github.com/smallerhand/python1.git <br/>

#### 이상 git의 제일 basic한 사용법이었습니다.<br/>
## 참고<br/>
> https://nolboo.kim/blog/2013/10/06/github-for-beginner/ <br/>
> https://git-scm.com/book/ko/v1/Git%EC%9D%98-%EA%B8%B0%EC%B4%88 <br/>

