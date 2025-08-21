-- Enable pgvector and create tables
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS accounts (
  id SERIAL PRIMARY KEY,
  domain TEXT UNIQUE NOT NULL,
  name TEXT,
  industry TEXT,
  size TEXT,
  tech_stack JSONB DEFAULT '{}'::jsonb,
  firmographics JSONB DEFAULT '{}'::jsonb,
  last_seen_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS signals (
  id SERIAL PRIMARY KEY,
  account_id INT REFERENCES accounts(id) ON DELETE CASCADE,
  type TEXT NOT NULL,
  severity INT NOT NULL,
  title TEXT NOT NULL,
  description TEXT NOT NULL,
  raw JSONB DEFAULT '{}'::jsonb,
  detected_at TIMESTAMPTZ DEFAULT NOW(),
  source TEXT
);

CREATE TABLE IF NOT EXISTS documents (
  id SERIAL PRIMARY KEY,
  account_id INT REFERENCES accounts(id) ON DELETE CASCADE,
  source TEXT,
  url TEXT,
  title TEXT,
  content TEXT,
  text_embedding VECTOR(1536),
  crawled_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS scores (
  id SERIAL PRIMARY KEY,
  account_id INT REFERENCES accounts(id) ON DELETE CASCADE,
  fit_score INT,
  intent_score INT,
  freshness_score INT,
  total_score INT,
  factors JSONB DEFAULT '{}'::jsonb,
  scored_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS outreach (
  id SERIAL PRIMARY KEY,
  account_id INT REFERENCES accounts(id) ON DELETE CASCADE,
  channel TEXT,
  subject TEXT,
  body TEXT,
  assets JSONB DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  status TEXT
);

CREATE TABLE IF NOT EXISTS alerts (
  id SERIAL PRIMARY KEY,
  account_id INT REFERENCES accounts(id) ON DELETE CASCADE,
  trigger TEXT,
  payload JSONB DEFAULT '{}'::jsonb,
  sent_at TIMESTAMPTZ DEFAULT NOW(),
  channel TEXT
);

-- Useful indexes
CREATE INDEX IF NOT EXISTS idx_documents_embedding ON documents USING ivfflat (text_embedding vector_l2_ops) WITH (lists = 100);
CREATE INDEX IF NOT EXISTS idx_signals_account ON signals(account_id);
CREATE INDEX IF NOT EXISTS idx_scores_account ON scores(account_id);
CREATE INDEX IF NOT EXISTS idx_outreach_account ON outreach(account_id);
