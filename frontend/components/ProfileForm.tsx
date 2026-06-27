"use client"

import { useState } from "react"
import { profileSchema, ProfileFormValues } from "@/schemas/profile"
import { submitProfile } from "@/actions/submitProfile"

type Gender = ProfileFormValues["gender"]

type FieldErrors = Partial<Record<keyof ProfileFormValues, string>>

const GENDER_OPTIONS: { value: Gender; label: string }[] = [
  { value: "male", label: "男性" },
  { value: "female", label: "女性" },
  { value: "other", label: "その他" },
]

export default function ProfileForm() {
  const [name, setName] = useState("")
  const [gender, setGender] = useState<Gender | "">("")
  const [age, setAge] = useState("")
  const [errors, setErrors] = useState<FieldErrors>({})
  const [submitting, setSubmitting] = useState(false)
  const [success, setSuccess] = useState(false)
  const [serverError, setServerError] = useState("")

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setServerError("")

    const parsed = profileSchema.safeParse({
      name,
      gender: gender || undefined,
      age: age === "" ? undefined : Number(age),
    })

    if (!parsed.success) {
      const fieldErrors: FieldErrors = {}
      for (const issue of parsed.error.issues) {
        const key = issue.path[0] as keyof ProfileFormValues
        if (!fieldErrors[key]) fieldErrors[key] = issue.message
      }
      setErrors(fieldErrors)
      return
    }

    setErrors({})
    setSubmitting(true)
    const result = await submitProfile(parsed.data)
    setSubmitting(false)

    if (result.success) {
      setSuccess(true)
      setName("")
      setGender("")
      setAge("")
    } else {
      setServerError(result.error)
    }
  }

  if (success) {
    return (
      <div className="rounded-lg bg-green-50 border border-green-200 p-6 text-center">
        <p className="text-green-700 font-semibold text-lg">送信が完了しました！</p>
        <button
          onClick={() => setSuccess(false)}
          className="mt-4 text-sm text-green-600 underline hover:text-green-800"
        >
          もう一度入力する
        </button>
      </div>
    )
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-6">
      {serverError && (
        <div className="rounded-lg bg-red-50 border border-red-200 px-4 py-3 text-red-700 text-sm">
          {serverError}
        </div>
      )}

      {/* 氏名 */}
      <div>
        <label htmlFor="name" className="block text-sm font-medium text-gray-700 mb-1">
          氏名 <span className="text-red-500">*</span>
        </label>
        <input
          id="name"
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="例: 山田 太郎"
          className={`w-full rounded-md border px-3 py-2 text-sm shadow-sm outline-none focus:ring-2 focus:ring-blue-500 ${
            errors.name ? "border-red-400" : "border-gray-300"
          }`}
        />
        {errors.name && <p className="mt-1 text-xs text-red-500">{errors.name}</p>}
      </div>

      {/* 性別 */}
      <div>
        <label htmlFor="gender" className="block text-sm font-medium text-gray-700 mb-1">
          性別 <span className="text-red-500">*</span>
        </label>
        <select
          id="gender"
          value={gender}
          onChange={(e) => setGender(e.target.value as Gender | "")}
          className={`w-full rounded-md border px-3 py-2 text-sm shadow-sm outline-none focus:ring-2 focus:ring-blue-500 bg-white ${
            errors.gender ? "border-red-400" : "border-gray-300"
          }`}
        >
          <option value="">選択してください</option>
          {GENDER_OPTIONS.map((opt) => (
            <option key={opt.value} value={opt.value}>
              {opt.label}
            </option>
          ))}
        </select>
        {errors.gender && <p className="mt-1 text-xs text-red-500">{errors.gender}</p>}
      </div>

      {/* 年齢 */}
      <div>
        <label htmlFor="age" className="block text-sm font-medium text-gray-700 mb-1">
          年齢 <span className="text-red-500">*</span>
        </label>
        <input
          id="age"
          type="number"
          value={age}
          onChange={(e) => setAge(e.target.value)}
          placeholder="例: 30"
          min={0}
          max={150}
          className={`w-full rounded-md border px-3 py-2 text-sm shadow-sm outline-none focus:ring-2 focus:ring-blue-500 ${
            errors.age ? "border-red-400" : "border-gray-300"
          }`}
        />
        {errors.age && <p className="mt-1 text-xs text-red-500">{errors.age}</p>}
      </div>

      <button
        type="submit"
        disabled={submitting}
        className="w-full rounded-md bg-blue-600 px-4 py-2 text-sm font-semibold text-white shadow hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
      >
        {submitting ? "送信中..." : "送信する"}
      </button>
    </form>
  )
}
