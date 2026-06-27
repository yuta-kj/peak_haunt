import type { Metadata } from "next"
import ProfileForm from "@/components/ProfileForm"

export const metadata: Metadata = {
  title: "プロフィール入力 | Peak Haunt",
}

export default function ProfilePage() {
  return (
    <main className="min-h-screen bg-gray-50 flex items-center justify-center px-4">
      <div className="w-full max-w-md bg-white rounded-xl shadow-md p-8">
        <h1 className="text-2xl font-bold text-gray-800 mb-2">プロフィール入力</h1>
        <p className="text-sm text-gray-500 mb-6">氏名・性別・年齢を入力してください。</p>
        <ProfileForm />
      </div>
    </main>
  )
}
