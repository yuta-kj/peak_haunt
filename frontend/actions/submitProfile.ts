"use server"

import { profileSchema, ProfileFormValues } from "@/schemas/profile"

type SubmitResult =
  | { success: true; id: number }
  | { success: false; error: string }

export async function submitProfile(data: ProfileFormValues): Promise<SubmitResult> {
  const parsed = profileSchema.safeParse(data)
  if (!parsed.success) {
    return { success: false, error: "入力内容が正しくありません" }
  }

  const baseUrl = process.env.API_BASE_URL ?? "http://localhost:8000"

  let res: Response
  try {
    res = await fetch(`${baseUrl}/api/v1/profiles`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(parsed.data),
    })
  } catch {
    return { success: false, error: "サーバーへの接続に失敗しました" }
  }

  if (!res.ok) {
    const body = await res.json().catch(() => null) as { detail?: string } | null
    const detail = body?.detail ?? `送信に失敗しました (${res.status})`
    return { success: false, error: detail }
  }

  const json = await res.json() as { id: number }
  return { success: true, id: json.id }
}
