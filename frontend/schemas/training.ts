import { z } from "zod"

export const trainingLogSchema = z.object({
  profileId: z.number().int().positive(),
  exercise: z.string().min(1, "種目名を入力してください").max(100),
  sets: z.number().int().min(1, "1セット以上を入力してください"),
  reps: z.number().int().min(1, "1回以上を入力してください"),
  load_kg: z.number().min(0, "0kg以上を指定してください"),
  memo: z.string().optional(),
})

export type TrainingLogFormValues = z.infer<typeof trainingLogSchema>

export interface TrainingLogItem {
  id: number
  profile_id: number
  excercise: string
  sets: number
  reps: number
  load_kg: number
  memo: string | null
}