1. sync 방식 db 
    a. db `connection` 정보를 기반으로 엔진생성
    b. `sessionmaker`클래스를 통해 해당 엔진으로 `session`객체 생성
    c. 만들어진 `session`을 genertate 방식으로 의존성 주입


2.  async 방식 db
    a. db `connection` 정보를 기반으로 엔진 생성
    b. `AsyncSession` 비동기 세션클래스를 사용해서  `session`객체 생성
    c. 만들어진 `session`을 genertate 방식으로 의존성 주입


===============================
1. alembic 만들때 async로 초기화 할 경우 `$ alembic init -t async migriatinos` 명령어 사용해서 명시적으로 async alembic.ini파일 생성하도록 만들자!

2. target_metadata 만들때는 `Base`를 모델이 있는 곳에서 가져와야한다!!!!! 그래야 마이그레이션 가능! 
