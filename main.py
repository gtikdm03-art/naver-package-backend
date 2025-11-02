from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import logging

from models import TravelPackage, SearchRequest, ApiResponse
from scraper import NaverPackageScraper

# 로깅 설정
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPI 앱 생성
app = FastAPI(
    title="네이버 패키지 여행 API",
    description="네이버 패키지 여행 검색 API",
    version="1.0.0"
)

# CORS 설정 (안드로이드 앱에서 접근 가능하도록)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 크롤러 인스턴스
scraper = NaverPackageScraper()

@app.get("/")
def read_root():
    """루트 엔드포인트"""
    return {
        "message": "네이버 패키지 여행 API",
        "version": "1.0.0",
        "endpoints": {
            "search": "/api/search",
            "docs": "/docs"
        }
    }

@app.get("/api/search", response_model=ApiResponse)
def search_packages(
    destination: str = Query(..., description="여행지 코드"),
    start_date: str = Query(..., description="출발일 (YYYY.MM.DD)"),
    end_date: str = Query(..., description="도착일 (YYYY.MM.DD)"),
    no_tips: bool = Query(True, description="노팁 여부"),
    no_shopping: bool = Query(True, description="노쇼핑 여부"),
    no_optional_tour: bool = Query(True, description="노옵션 여부"),
    product_type: str = Query("FPKG", description="상품 타입")
):
    """여행 패키지 검색"""
    try:
        logger.info(f"검색 요청: {destination}, {start_date} ~ {end_date}")
        
        # 크롤링 실행
        packages = scraper.search_packages(
            destination=destination,
            start_date=start_date,
            end_date=end_date,
            no_tips=no_tips,
            no_shopping=no_shopping,
            no_optional_tour=no_optional_tour,
            product_type=product_type
        )
        
        logger.info(f"검색 완료: {len(packages)}개 상품")
        
        return ApiResponse(
            success=True,
            data=packages,
            message=f"{len(packages)}개 상품을 찾았습니다"
        )
        
    except Exception as e:
        logger.error(f"검색 오류: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health_check():
    """헬스 체크"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)