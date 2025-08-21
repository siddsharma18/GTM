export default function ScoreBreakdown({ score }: { score: any }) {
	const f = score?.factors || {}
	return (
		<div className="text-sm grid grid-cols-2 gap-2">
			<div>Size: {f.size}</div>
			<div>Industry: {f.industry}</div>
			<div>Okta: {String(f.tech_okta)}</div>
			<div>AAD: {String(f.tech_aad)}</div>
			<div>Freshness (days): {f.freshness_days}</div>
		</div>
	)
}
