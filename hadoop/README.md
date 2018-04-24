## windows에 하둡 설치하기

<p>

### 1. 준비물
VirtualBox-5.1.6-110634-Win.exe
<br>
위 VirtualBox 설치
<br>
C:\hadoop 폴더에 아래 5개 파일 준비해놓는다.
</p>
<pre>
apache-hive-2.0.0-bin.tar.gz
CentOS-6.4-x86_64-bin-DVD1.iso
hadoop-2.7.2.tar.gz
jdk-7u80-linux-x64.tar.gz
protobuf-2.5.0.tar.gz
</pre>

<p>

### 2. 환경설정
virtualbox 파일> 환경설정> 입력> 가상머신> 호스트 키 조합 
<br>

확인 혹은 수정
<br>

환경설정> 네트워크> 호스트전용 네트워크> 편집모양 아이콘> 어댑터
<br>
여기에 있는 IPv4주소는 이 버츄얼머신 안에서만 사용.
<br>
DHCP 서버
<br>
서버사용 체크 확인
<br>
최저주소한계~최고주소한계 사이에서만 사용
<br>
간혹 충돌되면 이 주소 안에서 바꿔서 쓰면 됨.
</p>


<p>

### 3. 새로만들기(버츄얼박스 왼쪽위 버튼)
이름에 hadoopserver 입력
<br>
종류: 리눅스
<br>
버전: Red Hat(64 bit)
<br>
메모리 크기: 1기가 정도(일단은)
<br>
하드디스크: 지금 새 가상 하드 디스크 만들기
<br>
하드디스크 파일 종류: VDI
<br>
고정크기(좀 더 빠름)
<br>
파일 위치 및 크기: 16기가(일단)
<br>
만들기 클릭
<br>
왼쪽 날개에 hadoopserver가 생김.
</p>

<p>

### 4. 설정
일반> 고급> 클립보드 공유: 양방향/ 드래그앤드롭: 양방향
<br>
네트워크> 어댑터2> 네트워크 어댑터 사용하기 클릭
<br>
<b>
다음에 연결됨: 호스트 전용 어댑터
</b>
<br>
무작위모드: 모두 허용
<br>
케이블 연결됨 체크돼있는거 확인
<br>
공유폴더> 공유 추가 아이콘> 
<br>
폴더 경로: 기타 클릭, C:\hadoop 선택, 자동 마운트 클릭, ok
<br>
</p>

<p>

### 5. 시작 (버츄얼머신 위에 시작 버튼)
시동디스크 선택
<br>
오른쪽 폴더 모양 클릭
<br>
centos iso 파일 선택, 열기, 시작, 엔터
<br>
스킵
<br>
언어는 US English로
<br>
Yes
<br>
hostname: hadoopserver
<br>
Asia: Seoul
<br>
id/pw 입력
<br>
desktop으로 선택
<br>
customize add 선택, developer> development tools 설치
<br>
계정이름은 root(리눅스,유닉스 슈퍼계정은 항상 root), pw는 pw로
<br>
terminal 열어서 ls, cd, (다시) ls
</p>
<pre>
<code>
ls -al
ll
cd
</code>
</pre>

### 6. 네트워크 설정
<pre>
<code>
cd /etc/sysconfig/network-scripts
pwd
ls
(ifcfg-eth0, 1 있는지 확인)
cat ifcfg-eth0
cat ifcfg-eth1
(ifcfg-eth0의 onboot=no를 이따가 yes로 바꿀 것임)
(ifcfg-eth1의 onboot=no를 이따가 yes로 바꾸고, 
nm_controlled=yes는 놔두고, 
bootproto=dhcp를 none으로 바꾸고, 
NETMASK=255.255.255.0 추가,
IPADDR=192.168.56.101 추가)
</code>
</pre>
<p>
ifcfg-eth1의 역할은 vm안에 생성한 server들끼리 통신하기 위한 용도
</p>

<pre>
<code>
vi ifcfg-eth0
방향키로 원하는 위치로 가서 cw누르면 지워짐. 그리고 원하는 키워드 입력.

제일 아래줄로 가려면 
G
한 줄 추가하려면 
o
취소하고 나갈 때는
esc키 :q!
저장하고 나갈 때는
esc키 :wq

(저장하고 나서)
service network restart
(인터넷 되는지 확인)
cat /etc/hosts
vi /etc/hosts

(앞에서 customize add> development tools 선택 안 했으면)
yum -y install gcc make kernel-devel kernel sources kernel-headers
yum -y groupinstall "Development Tools"
</code>
</pre>

### 7. 확장
<p>
장치> 게스트 확장 CD이미지 삽입> 확장> run
<br>
terminal에서 reboot
<br>
방화벽 중지
<br>
iptables -L
<br>
iptables -F
<br>
iptables -L
<br>
ls /media/sf_hadoop
<br>
jdk설정
<br>
java -version
<br>
mkdir -p /usr/java
</p>

<pre>
파일 옮기기
<code>
[root@hadoopserver ~]# cp /media/sf_hadoop/jdk-7u80-linux-x64.tar.gz /usr/java
[root@hadoopserver ~]# cd /usr/java
[root@hadoopserver java]# ls
jdk-7u80-linux-x64.tar.gz
[root@hadoopserver java]# ll
total 149940
-rwxr-x---. 1 root root 153530841 Apr 24 15:49 jdk-7u80-linux-x64.tar.gz
[root@hadoopserver java]# 
</code>
</pre>

<pre>
압축 풀기
<code>
[root@hadoopserver java]# cd /usr/java
[root@hadoopserver java]# tar xvfz jdk-7u80-linux-x64.tar.gz 
</code>
</pre>

<pre>
<code>
vi /etc/profile
G
o
export JAVA_HOME=/usr/java/jdk1.7.0_80
export PATH=$PATH:$JAVA_HOME/bin
export CLASS_PATH="."
esc :wq
</code>
</pre>





