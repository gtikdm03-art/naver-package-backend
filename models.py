from pydantic import BaseModel
from typing import List, Optional

class TravelPackage(BaseModel):
    """여행 패키지 데이터 모델"""
    rank: int
    destination: str
    departureCity: str
    travelSchedule: str
    departureTime: str
    duration: str
    airline: str
    price: str
    productName: str

class SearchRequest(BaseModel):
    """검색 요청 모델"""
    destination: str
    startDate: str
    endDate: str
    noTips: bool = True
    noShopping: bool = True
    noOptionalTour: bool = True
    productType: str = "FPKG"

class ApiResponse(BaseModel):
    """API 응답 모델"""
    success: bool
    data: Optional[List[TravelPackage]] = None
    message: Optional[str] = None
