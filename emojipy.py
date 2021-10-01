from operator import itemgetter as ig
i = {
    '👋':'Hello',
    '🌎':'World',
    '🖨':'print',
    '🌜':'(',
    '🌛':')',
    '❕':'!',
    '❗':'!',
    '📎':'"',
    '🖇':"'",
    '🕳':' '
}
codigo = ig(
    '🖨','🌜','📎','👋','🕳','🌎','❕','📎','🌛'
    )(i)
codigo_traduzido = ''.join(codigo)
exec(codigo_traduzido)