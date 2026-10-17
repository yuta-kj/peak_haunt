"use server"

import { trainingLogSchema, TrainingLogFormValues, TrainingLogItem } from "@/schemas/training"

const API_BASE_URL = process.env.API_BASE_URL ?? "http://localhost:8000"

export async function createTrainingLog(data: TrainingLogFormValues) {
  const parsed = trainingLogSchema.safeParse(data)
  if (!parsed.success) {
    return { success: false, error: "入力内容が正しくありません" }
  }

  try {
    const res = await fetch(`${API_BASE_URL}/api/v1/training-logs`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        profile_id: parsed.data.profileId,
        exercise: parsed.data.exercise,
        sets: parsed.data.sets,
        reps: parsed.data.reps,
        weight_kg: parsed.data.load_kg,
        memo: parsed.data.memo || null,
      }),
    })

    if (!res.ok) {
      const errorData = await res.json().catch(() => null)
      return { success: false, error: errorData?.detail ?? "保存に失敗しました" }
    }

    const json = (await res.json()) as TrainingLogItem
    return { success: true, log: json }
  } catch {
    return { success: false, error: "バックエンドへの接続に失敗しました" }
  }
}

export async function fetchTrainingLogs(profileId: number): Promise<TrainingLogItem[]> {
  try {
    const res = await fetch(`${API_BASE_URL}/api/v1/training-logs/${profileId}`, {
      cache: "no-store",
    })
    if (!res.ok) return []
    return (await res.json()) as TrainingLogItem[]
  } catch {
    return []
  }
}