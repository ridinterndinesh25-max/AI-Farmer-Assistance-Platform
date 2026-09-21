import requests

from django.http import JsonResponse
from django.shortcuts import render


OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.2:latest"


def ai_assistant(request):

    if request.method == "POST":

        question = request.POST.get("question", "").strip()

        if not question:
            return JsonResponse({
                "success": False,
                "answer": "Please ask a farming-related question."
            })

        prompt = f"""
You are an AI Farmer Assistant for Indian farmers.

Help farmers with:
- Crops
- Crop diseases
- Weather
- Irrigation
- Fertilizers
- Pests
- Market prices
- Crop recommendations
- General farming problems

Give simple, practical and easy-to-understand answers.

Prefer Indian farming context.

If the farmer asks about serious crop disease or chemical treatment,
tell them to verify the treatment with a local agriculture expert.

Farmer's question:
{question}
"""

        try:

            response = requests.post(
                OLLAMA_URL,
                json={
                    "model": OLLAMA_MODEL,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=120
            )

            response.raise_for_status()

            data = response.json()

            answer = data.get(
                "response",
                "Sorry, I could not generate an answer."
            )

            return JsonResponse({
                "success": True,
                "answer": answer
            })

        except requests.exceptions.ConnectionError:

            return JsonResponse({
                "success": False,
                "answer": "Ollama is not running. Please start Ollama and try again."
            })

        except requests.exceptions.Timeout:

            return JsonResponse({
                "success": False,
                "answer": "AI response is taking too long. Please try again."
            })

        except Exception as e:

            return JsonResponse({
                "success": False,
                "answer": f"AI service error: {str(e)}"
            })

    return render(
        request,
        "ai_assistant/assistant.html"
    )