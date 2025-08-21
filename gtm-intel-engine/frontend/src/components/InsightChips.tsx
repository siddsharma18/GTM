export default function InsightChips({ signals }: { signals: any[] }) {
	return (
		<div className="flex gap-2 flex-wrap">
			{signals.map((s, i) => (
				<span key={i} className={`px-2 py-1 text-xs rounded ${s.severity >= 4 ? 'bg-red-100 text-red-700' : 'bg-yellow-100 text-yellow-700'}`}>
					{s.type}
				</span>
			))}
		</div>
	)
}
