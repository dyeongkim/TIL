# 운영체제/OperatingSystem
## 4. 파일 시스템
### 4.1 파일 시스템 구성요소
- 파일
    - 데이터 저장의 기본 단위
- 디렉토리
    - 계층 구조 내에서 파일을 구성하는데 사용되는 컨테이너
    - 효율적으로 탐색할 수 있도록 트리와 같은 구조를 만듬

- 메타데이터
    - 파일과 디렉터리를 관리하고 설명하기 위해 저장하는 추가 정보
    - 파일 크기, 생성 및 수정 시간, 액세스 권한, 소유권 정보와 같은 속성

### 4.2 접근 방법
파일에서 데이터를 읽고 쓰기 위한 다양한 액세스 방법

- 순차 접근(Sequential Access)   
파일의 처음부터 선형적이고 순차적인 방식으로 데이터를 읽거나 쓰는 방법
    - 파일의 정보가 레코드 순서대로 처리된다.
    - 현재 위치에서 읽거나 쓰면 Offset이 자동으로 증가
    - 뒤로 돌아가기 위해선 되감기가 필요.
    - 대규모 데이터 블록 읽기/쓰기 적합

- 직접 접근(Random Access)   
직접 액세스를 사용하면 파일 내의 모든 위치에서 데이터를 읽거나 쓸 수 있다.   
    - 파일의 레코드를 임의의 순서로 접근할 수 있다.
    - 디스크모델에 기반을 두고 있다.
    - 무작위 파일 블럭에 대한 임의 접근을 허용
    - 데이터베이스 관리에 유용
- 색인 접근(Index Access)   
논리적 파일 위치를 물리적 저장 위치에 매핑하는 인덱스를 사용하여 데이터 액세스
    - 파일에서 레코드를 찾기 위해 색인(Index)를 먼저 찾고 그에 대응되는 포인터를 얻는다.
    - 파일 시스템의 inode 기반 ext 계열과 같은 인덱스 할당 방법을 사용하는 시스템에 사용


### 4.3 할당 방법
파일을 저장하기 위해 저장 장치에 공간을 할당하는 방법

- 연속 할당
    - 파일이 연속된 스토리지 블록에 저장
    - 한 번의 연속 읽기/쓰기 작업으로 전체 파일에 액세스 가능.
    - 조각화를 줄이고 선능을 향상시킴
    - 시간이 지날수록 여유 공간이 조각화 된다.(외부 조각화 발생)

- 링크 할당
    - 파일을 데이터 블록의 링크된 목록으로 저장
    - 각 블록은 파일의 다음 블록에 대한 포인터를 포함
    - 파일 시스템이 파일의 특정 부분에 액세스 하기위해 블록 목록을 통과해야 해서 대용량 파일의 경우 액세스 시간이 느려진다.
    
    - 파일 블록을 저장 장치 위치에 매핑하는 inode 같은 인덱스 구조를 사용.
    - 연속 할당과 링크 할당의 장점을 결합하여 효율적인 액세스와 파일을 쉽게 늘릴 수 있다.
    - 인덱스 할당은 ext2, ext3, ext4와 같은 많은 최신 파일 시스템에서 사용

### 4.4 파일 시스템 구성
#### 1. 디렉토리 구조
- 단일 레벨 디렉토리
    - 계층 구조 없이 모든 파일과 디렉토리를 동일한 레벨에 저장
    - 간단한 구조는 구현하고 이해하기 쉽지만 파일과 디렉토리의 수가 증가하면 관리가 어렵다.
- 2단계 디렉토리
    - 파일과 디렉토리를 각 사용자별로 별도의 디렉토리로 구성
    - 각 사용자는 자신의 모든 파일과 하위 디렉토리가 들어 있는 최상위 디렉토리를 가진다.
    - 다른 사용자의 데이터를 간섭하지 않고 자신의 파일과 디렉토리를 독립적으로 관리
- 트리 구조 디렉토리
    - 다른 디렉토리를 포함하는 디렉토리가 있는 계층 구조
    - 직관적이고 유연하게 구성할 수 있다.
    - 대부분의 최신 파일 시스템 구조
- 비순환 그래프 디렉토리
    - 디렉토리가 다른 디렉토리에 대한 참조, 링크를 포함할 수 있도록 방향성 비순환 그래프를 형성
    - 데이터 복제 없이 여러 디렉토리 간에 파일과 디렉토리 공유 가능
    - 파일 시스템에서 주기를 처리하고 참조 수를 유지해야해서 더 복잡

#### 2. 여유공간 관리
새 파일과 디렉토리를 위한 공간을 할당하기 위해 저장 장치의 여유 공간을 추척해야 함.

- 비트맵
    - 스토리지의 각 블록을 비트로 표시하여 여유 공간인지 할당 공간인지 나타냄
    - 간결하고 효율적인 방법을 제공하여 파일 시스템에서 할당 가능 블록을 빠르게 찾을 수 있도록 한다.
    - 큰 저장 장치를 효율적으로 관리하기 위해 버디 시스템이나 확장 등 추가적인 데이터 구조나 기술이 필요

- Linked List
    - 여유 공간은 블록의 연결된 목록으로 구성
    - 각 블록은 다음 여유 블록에 대한 포인터를 포함
    - 연결된 목록은 여유 공간을 관리하는 간단하고 동적인 방법을 제공
    - 할당에 적합한 블록을 찾기 위해 목록을 탐색해야 해서 시간이 느려질 수 있음.
- Grouping(그룹화)
    - 여유 블록을 클러스터로 구성하여 개별 블록 관리의 오버헤드를 줄임
    - 파일 시스템이 전체 클러스터를 한번에 할당하거나 할당 해제 가능(할당 성능 향샹)
    - 부분적으로 사용되는 클러스터가 공간을 비효율적으로 소비하여 내부 조각화를 초래

#### 파일 시스템 성능
- 캐싱
    - 자주 액세스 하는 데이터를 메모리에 저장하여 디스크 액세스의 필요성을 줄이는 것
    - 자주 액세스 하는 데이터, 메타데이터 및 디렉토리 항목을 저장하여 전반적인 성능 향상

- 프리패칭
    - 향후 데이터 액세스 패턴을 예측하여 데이터가 필요하기 전에 미리 캐시에 데이터를 로드하는 기술
    - 파일 시스템 작업의 지연 시간을 줄이고 전반적인 성능 개선

- 저널링
    - 일부 파일 시스템에서 안정성을 개선하고 정전으로부터 복구하기 위해 사용하는 기술
    - 파일 시스템 작업을 실제 데이터 구조에 적용하기 전에 로그에 기록하는 것을 포함