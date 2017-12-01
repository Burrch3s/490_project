// sound file
me.sourceDir() + "/slap.wav" => string filename1;
me.sourceDir() + "/whack.wav" => string filename2;
me.sourceDir() + "/kick.wav" => string filename3;
me.sourceDir() + "/jab.wav" => string filename4;
me.sourceDir() + "/upper.wav" => string filename5;

if( me.args() ) me.arg(0) => filename1;

// the patch 
SndBuf buf => dac;

0.0 =>  float num;
Std.rand2(0,1000) => num;
num % 5 => num;
<<< num >>>;

if( num == 0.0 )
{
// load the file
filename1 => buf.read;

0 => buf.pos;
350::ms => now;
}

if( num == 1.0 )
{
// load the file
filename2 => buf.read;

0 => buf.pos;
450::ms => now;
}

if( num == 2.0 )
{
// load the file
filename3 => buf.read;

0 => buf.pos;
400::ms => now;
}

if( num == 3.0 )
{
// load the file
filename4 => buf.read;

0 => buf.pos;
400::ms => now;
}

if( num == 4.0 )
{
// load the file
filename5 => buf.read;

0 => buf.pos;
400::ms => now;
}

