import { z } from "zod"

export const profileSchema = z.object({
  name: z.string().min(1, "氏名を入力してください").max(100, "100文字以内で入力してください"),
  gender: z.enum(["male", "female", "other"], {
    required_error: "性別を選択してください",
    invalid_type_error: "性別を選択してください",
  }),
  age: z
    .number({ invalid_type_error: "年齢を入力してください" })
    .int("整数を入力してください")
    .min(0, "0以上の値を入力してください")
    .max(150, "150以下の値を入力してください"),
})

export type ProfileFormValues = z.infer<typeof profileSchema>
