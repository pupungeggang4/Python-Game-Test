import pygame

# 1. Pygame 초기화
pygame.init()

# 2. 창 크기 설정 및 생성 (가로 800, 세로 600)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame 기본 창")

# 3. 게임 루프 제어 변수
running = True

# 4. 메인 루프 (창이 켜져 있는 동안 무한 반복)
while running:
    # 이벤트 처리 (마우스 클릭, 키보드 입력 등 감지)
    for event in pygame.event.get():
        # 사용자가 창 닫기 버튼(X)을 누르면 루프 종료
        if event.type == pygame.QUIT:
            running = False

    # 화면을 검은색으로 채우기
    screen.fill((0, 0, 0))
    
    # 화면 업데이트
    pygame.display.flip()

# 5. Pygame 종료
pygame.quit()

