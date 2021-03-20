# Git

> Git은 분산버전관리시스템(DVCS)이다. Distributed Version Control System
>
> 소스코드의 버전 및 이력을 관리할 수 있다.

## 준비하기

윈도우에서 git을 활용하기 위해서 [git bash](http://https://gitforwindows.org/)를 설치한다.

git을 활용하기 위해서 GUI 툴인 `source tree`,`github desktop`등을 활용할 수도 있다.

초기 설치를 완료한 이후에 컴퓨터에 `author`정보를 입력한다.

```bash
$ git config --global user.name {user name}
$ git config --global user.email {user email}
```

## 로컬 저장소(repository) 활용하기

### 1. 저장소 초기화

```bash
$ git init
Initialized empty Git repository in C:/Users/student/Desktop/TIL/.git/
```

* `.git`폴더가 생성되며, 여기에 git과 관련된 모든 정보가 저장된다.
* git bash에 `(master)` 라고 표시되는데, 이는 현재 `master` branch에 있다는 뜻이다.

### 2. `add`

`working directory`, 즉 작업 공간에서 변경된 사항을 이력으로 저장하기 위해서는 반드시 `staging area`를 거쳐야한다. (스냅샷을 기록하기 위한 파일들을 선택하는 작업)

```bash
$ git add markdown.md # 특정 파일
$ git add images/ # 특정 폴더
$ git add . # 현재 디렉토리
```

* `add` 전 상태

```bash
$ git status
On branch master

No commits yet

# 트래킹 되고 있지 않는 파일들
# => commit 이력에 한번도 담기지 않은 파일들
Untracked files:
# 커밋될 것들에 포함시키려면 add 명령어를 사용
  (use "git add <file>..." to include in what will be committed)
        markdown.md
# 아직 커밋될 것들은 없지만
# untracked files은 존재한다.
nothing added to commit but untracked files present (use "git add" to track)

```

* `add` 후 상태

```bash
$ git status
On branch master

No commits yet
# 커밋될 변화들
# => staging area에 있는 파일들

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   markdown.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        git.md

```

### 3. `Commit`

commit은 이력을 확정짓는 명령어로, 해당 시점의 스냅샷을 기록한다.

커밋시에는 반드시 메시지를 작성 해야하며, 메시지는 변경사항을 알 수 있도록 명확하게 작성한다.

```bash
$ git commit -m '마크다운 정리'
[master (root-commit) 5313249] 마크다운 정리
 1 files changed, 104 insertions(+)
 create mode 100644 markdown.md
```

커밋 이후에는 아래의 명령어를 통해 지금까지 작성된 이력을 확인한다.

```bash
$ git log
commit 5313249e0c5aa5e9a2c5d77d44b3e73434617cfc (HEAD -> master)
Author: sinclairjang <edujason-hphk@gmail.com>
Date:   Thu Dec 26 14:34:35 2019 +0900

    마크다운 정리

$ git log --oneline
5313249 (HEAD -> master) 마크다운 정리
```

커밋은 해시값을 바탕으로 구분된다.

## 원격 저장소(remote repository) 활용하기

원격 저장소 기능을 제공하는 다양한 서비스 중에 github을 기준으로 설명한다.

### 0. 준비사항

* Github에 repository생성

### 1. 원격 저장소 등록

```bash
$ git remote add origin {github url}
```

* 원격저장소(`remote`)로 `origin`이라는 이름으로 `github url`을 등록(`add`)한다.
* 등록된 원격 저장소 목록을 보기 위해서는 아래의 명령어를 활용한다.

``` bash
$ git remote -v
origin  https://github.com/edujason-hphk/TIL.git (fetch)
origin  https://github.com/edujason-hphk/TIL.git (push)
```

### 2. `push` - 원격저장소 업로드

```bash
$ git push origin master
```

`origin`으로 설정된 원격저장소에 `master` 브랜치로 업로드(`push`)

이후 변경사항이 생길 때마다, `add`-`commit`,`push`를 반복하면 된다.

그리고, 항상 모든 명령어 이후에 연관된 상태를 확인하자.

`status`, `log`, `remote -v`