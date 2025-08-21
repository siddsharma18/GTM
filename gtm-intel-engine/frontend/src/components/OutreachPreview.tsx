import CopyButton from "./CopyButton"
export default function OutreachPreview({ variants }: { variants: any[] }) {
	return (
		<div className="space-y-3">
			{variants.map((v, i) => (
				<div key={i} className="border p-3 rounded">
					<p className="font-semibold">{v.subject || 'LinkedIn'}</p>
					<div className="flex justify-between items-center mb-1"><span className="font-mono text-xs opacity-70">{v.subject || ""}</span><CopyButton text={v.body} /></div><pre className="whitespace-pre-wrap text-sm">{v.body}</pre>
				</div>
			))}
		</div>
	)
}
