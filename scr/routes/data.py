from fastapi import FastAPI , APIRouter , Depends , UploadFile , status
from helpers.config import get_settings , Settings
from controllers import DataController
from fastapi.responses import JSONResponse
data_router = APIRouter(
    prefix = "/api/v1/data",
    tags = ["api_v1" , "data"]
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id ,file:UploadFile , app_setting : Settings = Depends(get_settings)):

    # validation file properties
    is_valid , result_signal = DataController().validaate_uploaded_type(file=file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"signal": result_signal}
        )

    return {
        "signal": result_signal
    }