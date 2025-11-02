from typing import List
import time
import random
from models import TravelPackage

class NaverPackageScraper:
    """네이버 패키지 여행 크롤러"""
    
    def __init__(self):
        self.base_url = "https://package.naver.com"
    
    def search_packages(
        self,
        destination: str,
        start_date: str,
        end_date: str,
        no_tips: bool = True,
        no_shopping: bool = True,
        no_optional_tour: bool = True,
        product_type: str = "FPKG"
    ) -> List[TravelPackage]:
        """
        여행 패키지 검색
        
        TODO: 실제 네이버 사이트 크롤링 구현
        현재는 Mock 데이터 반환
        """
        
        return self._get_mock_data(destination)
    
    def _get_mock_data(self, destination: str) -> List[TravelPackage]:
        """Mock 데이터 생성"""
        
        destination_name = self._get_destination_name(destination)
        
        time.sleep(random.uniform(0.5, 1.5))
        
        packages = [
            TravelPackage(
                rank=1,
                destination=destination_name,
                departureCity="인천",
                travelSchedule="2026.05.30 ~ 2026.08.30",
                departureTime="09:00",
                duration="3박 4일",
                airline="대한항공",
                price="899,000",
                productName=f"[{destination_name}] 자유여행 3박4일 (노쇼핑/노팁/노옵션)",
            ),
            TravelPackage(
                rank=2,
                destination=destination_name,
                departureCity="부산",
                travelSchedule="2026.05.30 ~ 2026.08.30",
                departureTime="10:30",
                duration="4박 5일",
                airline="아시아나항공",
                price="1,199,000",
                productName=f"[{destination_name}] 완전자유 4박5일 프리미엄 패키지",
            ),
            TravelPackage(
                rank=3,
                destination=destination_name,
                departureCity="인천",
                travelSchedule="2026.05.30 ~ 2026.08.30",
                departureTime="14:00",
                duration="3박 4일",
                airline="진에어",
                price="699,000",
                productName=f"[{destination_name}] 알뜰 자유여행 3박4일 (노팁)",
            ),
            TravelPackage(
                rank=4,
                destination=destination_name,
                departureCity="청주",
                travelSchedule="2026.05.30 ~ 2026.08.30",
                departureTime="11:00",
                duration="4박 5일",
                airline="티웨이항공",
                price="1,099,000",
                productName=f"[{destination_name}] 청주출발 4박5일 자유여행",
            ),
            TravelPackage(
                rank=5,
                destination=destination_name,
                departureCity="인천",
                travelSchedule="2026.05.30 ~ 2026.08.30",
                departureTime="16:30",
                duration="5박 6일",
                airline="대한항공",
                price="1,499,000",
                productName=f"[{destination_name}] 럭셔리 5박6일 완전자유 프리미엄",
            ),
            TravelPackage(
                rank=6,
                destination=destination_name,
                departureCity="인천",
                travelSchedule="2026.05.30 ~ 2026.08.30",
                departureTime="13:00",
                duration="4박 5일",
                airline="제주항공",
                price="849,000",
                productName=f"[{destination_name}] 가성비 4박5일 자유여행",
            ),
            TravelPackage(
                rank=7,
                destination=destination_name,
                departureCity="부산",
                travelSchedule="2026.05.30 ~ 2026.08.30",
                departureTime="15:30",
                duration="3박 4일",
                airline="에어부산",
                price="799,000",
                productName=f"[{destination_name}] 부산출발 알뜰 3박4일",
            ),
            TravelPackage(
                rank=8,
                destination=destination_name,
                departureCity="인천",
                travelSchedule="2026.05.30 ~ 2026.08.30",
                departureTime="11:30",
                duration="5박 6일",
                airline="아시아나항공",
                price="1,599,000",
                productName=f"[{destination_name}] 프리미엄 5박6일 완전패키지",
            )
        ]
        
        return packages
    
    def _get_destination_name(self, code: str) -> str:
        """여행지 코드를 이름으로 변환"""
        destinations = {
            "JP": "일본",
            "OSA": "오사카",
            "TYO": "도쿄",
            "SPK": "삿포로",
            "OKA": "오키나와",
            "FUK": "후쿠오카",
            "TSJ": "대마도",
            "ES": "스페인",
            "PT": "포르투갈",
            "FR": "프랑스",
            "IT": "이탈리아",
            "TH": "태국",
            "VN": "베트남",
            "US": "미국",
            "GB": "영국",
            "DE": "독일",
            "CN": "중국",
            "PH": "필리핀"
        }
        return destinations.get(code, code)
