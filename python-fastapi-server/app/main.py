# generated by fastapi-codegen:
#   filename:  swagger.yaml
#   timestamp: 2020-11-28T07:29:34+00:00

from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .models import (
    SlotValidationFiniteValuesRequest,
    SlotValidationNumericRequest,
    SlotValidationResult,
    Time,
)

try:
    from .implementation import Implementation

    implementation = Implementation()
except ModuleNotFoundError as e:
    raise NotImplementedError

app = FastAPI(
    title="Basket",
    description="REST API doc for Basket.",
    contact="{'email': 'akuma5157@gmail.com'}",
    version="0.1",
)

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/time/', response_model=Time)
def get_time() -> Time:
    return implementation.get_time()


@app.post('/validate-finite-values-entity/', response_model=SlotValidationResult)
def validate_finite_values_entity(
    body: SlotValidationFiniteValuesRequest = None,
) -> SlotValidationResult:
    return implementation.validate_finite_values_entity(body)


@app.post('/validate-numeric-entity/', response_model=SlotValidationResult)
def validate_numeric_entity(
    body: SlotValidationNumericRequest = None,
) -> SlotValidationResult:
    return implementation.validate_numeric_entity(body)
