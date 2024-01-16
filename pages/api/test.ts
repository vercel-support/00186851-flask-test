import type { NextApiRequest, NextApiResponse } from 'next'

export default async function handler(req: NextApiRequest, res: NextApiResponse)
{
    const { details } = req.query
    res.status(200).json({ response: 'node route test' })
}
