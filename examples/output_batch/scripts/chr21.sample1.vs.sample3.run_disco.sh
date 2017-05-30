source scripts/bashrc_genomedisco
/srv/gsfs0/projects/snyder/oursu/software/anaconda2/mypython/bin/python /srv/gsfs0/projects/snyder/oursu/software/git/public_genomedisco/genomedisco/genomedisco/__main__.py --m1 /srv/gsfs0/projects/snyder/oursu/software/git/public_genomedisco/genomedisco/examples/output_batch/data/edges/sample1/sample1.chr21.gz --m2 /srv/gsfs0/projects/snyder/oursu/software/git/public_genomedisco/genomedisco/examples/output_batch/data/edges/sample3/sample3.chr21.gz --m1name sample1 --m2name sample3 --node_file /srv/gsfs0/projects/snyder/oursu/software/git/public_genomedisco/genomedisco/examples/output_batch/data/nodes/Nodes.w40000.bed.gz.chr21.gz --outdir /srv/gsfs0/projects/snyder/oursu/software/git/public_genomedisco/genomedisco/examples/output_batch/results/sample1.vs.sample3 --outpref chr21 --m_subsample NA --approximation 1000000 --norm sqrtvc --method RandomWalks --tmin 3 --tmax 7