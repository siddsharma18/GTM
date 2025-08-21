import { useState } from 'react'

export default function CopyButton({ text }: { text: string }) {
	const [copied, setCopied] = useState(false)
	return (
		<button
			onClick={async () => {
				await navigator.clipboard.writeText(text)
				setCopied(true)
				setTimeout(() => setCopied(false), 1500)
			}}
			className="text-xs px-2 py-1 border rounded hover:bg-gray-50"
		>
			{copied ? 'Copied' : 'Copy'}
		</button>
	)
}
