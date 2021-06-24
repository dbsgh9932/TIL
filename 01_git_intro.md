# Git 초기 설정

### 커밋 작성자(author) 설정

##### 커밋을 작성한 사람을 알게 하기 위해

* `$ git config --global user.email "메일주소"`
  `$ git config --global user.name "유저네임"`

##### 지정된 설정 확인

* `$ git config --global -l`
  `$ git config --global --list`

##### 커밋 편집기 변경

* `$ git config --global core.editor "code --wait"`
  * 해당 명령어는 반드시 vscode가 설치되어 있어야 함



# Git Basic

### 로컬 저장소 설정

* `$ git init`
  `Initialized empty Git repository in C:/Users/student/Desktop/git_class`
  `student@M172 MINGW64 ~/Desktop/git_class (master)`
  * 폴더에 git저장소를 초기화 하면 `.git` 숨김 폴더가 생성되고 bash에는 `master` 가 표기됨

> git 저장소 내에 또다른 git 저장소를 만들면 안됨 !!git init 명령어를 입력할 때, (master)가 있으면 절대! 입력하지 말 것!

### add

* `$ git add 파일명`
  `$ git add . # 현재 디렉토리(하위 디렉토리)`
  `$ git add a.txt # 특정 파일`
  `$ git add my_folder/ # 특정 폴더`
  * `working directory` 상태의 파일을`staging area`상태로 변경
  * 커밋을 위한 파일 및 폴더들을 추가하는 명령어

### status

* `$ git status` 
  `On branch master`
  `No commits yet`
  `Changes to be committed: # 커밋 예정인 변경사항(staging area)`
  	`(use "git rm --cached <file>..." to unstage)`
  			`new file:  a.txt`
  `Untracked files: # 트래킹 되고 있지 않은 파일`
  	`(use "git add <file>..." to include in what will be committed)`
  			`b.txt`
* working directory, staging area 공간의 파일 상태를 확인할 수 있다.

> 모든 정보는 git status 에 있다. ( 위는 a.txt와 b.txt를 만들고 a.txt만 add한 상황)

### commit

* `$ git commit -m "first commit"` : 커밋을 통해 하나의 버전으로 기록
  * 현재 변경사항들을 잘 나타낼 수 있도록 작성을 권장

### log

* 커밋이 완료 되면, 잘 기록되었는지 확인!
* `$ git log`
  `$ git log -1 # 최근 몇개까지 보여주는 옵션`
  `$ git log --oneline # 한줄로 보여주는 옵션`

### git show

* 현재 커밋의 변경 기록을 확인하기

### git diff 커밋아이디1 커밋아이디2

* 커밋들 사이에 변경 사항을 확인 할 수 있음
* `git diff 9b15 539d`

