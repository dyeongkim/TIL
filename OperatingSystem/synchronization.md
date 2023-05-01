# 운영체제/OperatingSystem
## 6. 동시성과 동기화
> 동시성이란 다중 작업의 동시 실행을 말한다.

병렬 처리 또는 
### 6.1 동기화 메커니즘
> 동시 작업의 실행을 조정하고 제어하기 위해 운영체제에서 사용하는 도구 및 기술

- 세마포어
    - 사용 가능한 리소스 수를 나타내는 카운터를 유지 관리하여 공유 리소스에 대한 엑세스를 제어
    - 동시 작업 간의 상호 배제 및 신호/대기 작업을 구현하는데 사용
- 뮤텍스(상호배제)
    - 공유 리소스에 대한 베타적 액세스를 보장하기 위한 동기화 프리미티브(synchronization primitive)
    - 잠금/해제 작업을 제공하여 여러 작업이 동일한 리소스에 동시에 액세스 못하도록 경합 상태 방지
- 모니터
    - 단일 개체 내에서 공유 데이터 및 동기화 프리미티브를 캡슐화 하는 동기화 구조
    - 공유 리소스에 대한 액세스를 관리
    - 조건 변수 및 기본 제공 잠금/해제 작업을 사용하여 동시 작업 실행을 조정

- 조건 변수
    - 작업이 진행하기 전에 특정 조건이 충족될 때까지 기다릴 수 있도록 뮤텍스 혹은 모니터와 함께 사용되는 동기화 프리미티브
    - 효율적인 생산자-소비자 패턴, 신호/대기 작업 및 기타 복잡한 동기화 시나리오 구현

<br>

---

<br>

### 6.2 동시성 문제

- 경쟁 조건
    - 프로그램의 동작이 동시 작업이 실행되는 순서와 같은 이벤트의 상대적 타이밍에 따라 달라질 때 발생
    - 예측할 수 없는 결과와 데이터 손상으로 이어질 수 있으므로 감지 및 재현이 어렵다.
- 교착 상태
    - 각 작업이 집합의 다른 작업이 보유한 리소스를 기다리고 있기 때문에 일련의 작업을 진행할 수 없는 상황
    - 교착상태로 인해 시스템이 응답하지 않게 될 수 있다.
- 기아
    - 다른 작업에 공유 리소스에 대한 액세스 권한이 지속적으로 부여되어 작업이 무기한 지연될 때 발생
    - 시스템 성능과 공정성을 저하시킬 수 있다.
    - 모든 작업이 공유 리소스에 액세스할 수 있는 동등한 기회를 보장하는 설계를 하는것이 필수

### 6.3 예약 및 동시성

- 선도착 선처리 기법(FCFS : First Come First Served)
    - 먼저 생성된, 먼저 준비 상태로 들어온 프로세스 먼저 실행
- 최단작업 우선 기법(SJF : Shortest Job First)
    - 준비 상태에 있는 프로세스 중 CPU 사용 시간이 가장 짧은 것부터 실행
- 순환 순서 기법(RR : Round Robin)
    - 여러 프로세스가 돌아가면서 CPU를 조금씩 차지
- 우선순위 스케줄링
    - 준비 큐에 프로세스가 도착하면, 도착한 프로세스의 우선순위와 현재 실행중인 프로세스의 우선순위를 비교하여 우선순위가 높은 프로세스에 프로세서를 할당
- 다단계 피드백 큐(MFQ)
    - 우선순위 별로 준비 큐를 분리
    - 우선순위 높은 큐를 모두 처리한 후 낮은 우선순위 큐 처리