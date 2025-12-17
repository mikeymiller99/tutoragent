from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any, Literal

# ---------- Core enums / literals ----------

Difficulty = Literal["Beginner", "Intermediate", "Advanced"]
Mode = Literal["Explain", "Debug", "Practice"]
Language = Literal["HTML", "CSS", "JavaScript", "Unknown"]

# ---------- API request ----------

class TutorRequest(BaseModel):
    user_goal: str = Field(min_length=1, description="What the learner wants help with")
    code_snippet: Optional[str] = Field(
        default=None,
        description="Optional code provided by the learner"
    )
    difficulty: Difficulty = "Beginner"
    mode: Mode = "Debug"
    constraints: List[str] = Field(
        default_factory=list,
        description="Instructional or safety constraints"
    )

# ---------- Classification ----------

class Classification(BaseModel):
    language: Language
    intent: Mode
    skill_level: Difficulty
    risk_flags: List[str] = Field(default_factory=list)

# ---------- Analysis ----------

class Issue(BaseModel):
    title: str
    severity: Literal["low", "medium", "high"]
    evidence: str
    suggestion: str

class AnalysisReport(BaseModel):
    issues_found: List[Issue] = Field(default_factory=list)
    notes: str = ""

# ---------- Tutor output ----------

class TutorDraft(BaseModel):
    summary: str
    explanation: str
    fixed_code: Optional[str] = None
    next_exercise: str

# ---------- Self-check ----------

class SelfCheck(BaseModel):
    passes: bool
    failures: List[str] = Field(default_factory=list)
    notes: str = ""

# ---------- Agent trace / instrumentation ----------

class StepResult(BaseModel):
    step_name: str
    output: Dict[str, Any]
    ok: bool = True
    error: Optional[str] = None

class AgentTrace(BaseModel):
    request: Dict[str, Any]
    steps: List[StepResult]
    final: Dict[str, Any]

# ---------- API response ----------

class TutorResponse(BaseModel):
    summary: str
    explanation: str
    fixed_code: Optional[str] = None
    issues_found: List[Issue] = Field(default_factory=list)
    next_exercise: str
    rubric_score: Dict[str, Any]
    meta: Dict[str, Any]
